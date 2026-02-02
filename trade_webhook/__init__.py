import logging
import azure.functions as func

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info("trade_webhook triggered")

    try:
        body = req.get_json()
        logging.info("Payload: %s", body)
    except Exception:
        logging.info("No JSON body (or invalid JSON).")

    return func.HttpResponse("OK", status_code=200)
