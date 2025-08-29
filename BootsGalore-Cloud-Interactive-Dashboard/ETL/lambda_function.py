import os, json, csv, io, time, urllib.parse, logging
import boto3

logger = logging.getLogger()
logger.setLevel(logging.INFO)

dynamodb = boto3.resource("dynamodb")
s3 = boto3.client("s3")

TABLE_NAME = os.environ.get("TABLE_NAME", "BootsBrandSecondWord")

def second_word(value: str):
    if not value:
        return None
    parts = str(value).strip().split()
    return parts[1] if len(parts) > 1 else None

def _get_csv_reader(text: str):
    sample = text[:2048]
    try:
        dialect = csv.Sniffer().sniff(sample, delimiters=";,")
        logger.info("Detected delimiter: %r", dialect.delimiter)
    except Exception:
        header = sample.splitlines()[0] if sample else ""
        if header.count(";") >= header.count(","):
            class _Dialect(csv.excel):
                delimiter = ";"
            dialect = _Dialect()
            logger.info("Fallback delimiter: ';'")
        else:
            dialect = csv.excel
            logger.info("Fallback delimiter: ','")
    return csv.DictReader(io.StringIO(text), dialect=dialect)

def lambda_handler(event, context):
    table = dynamodb.Table(TABLE_NAME)
    records = event.get("Records", [])
    if not records:
        logger.warning("No records in event")
        return {"inserted": 0}

    total_inserted = 0

    for rec in records:
        bucket = rec["s3"]["bucket"]["name"]
        key = urllib.parse.unquote_plus(rec["s3"]["object"]["key"])
        logger.info(f"Processing s3://{bucket}/{key}")

        obj = s3.get_object(Bucket=bucket, Key=key)
        body = obj["Body"].read()
        text = body.decode("utf-8-sig", errors="ignore")

        reader = _get_csv_reader(text)
        if "Brand Preference" not in reader.fieldnames:
            raise KeyError("Column 'Brand Preference' not found. Found: " + ", ".join(reader.fieldnames or []))

        count = 0
        for i, row in enumerate(reader, start=1):
            token = second_word(row.get("Brand Preference"))
            if not token:
                continue
            record_id = f"{key}#{i}"
            item = {
                "record_id": record_id,
                "brand_second_word": token,
                "source_key": key,
                "row_number": i,
                "ts": int(time.time()),
            }
            table.put_item(Item=item)
            count += 1

        total_inserted += count
        logger.info(f"Inserted {count} rows from {key}")

    return {"inserted": total_inserted}

