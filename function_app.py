import azure.functions as func

app = func.FunctionApp(http_auth_level=func.AuthLevel.FUNCTION)

@app.route(route="trade_webhook", methods=["POST"])
def trade_webhook(req: func.HttpRequest) -> func.HttpResponse:
    try:
        payload = req.get_json()
    except Exception:
        payload = None

    func_logger = func.get_logger("trade_webhook")
    func_logger.info(f"Webhook received: {payload}")

    return func.HttpResponse("OK", status_code=200)
