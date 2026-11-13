import time
def process_webhook(payload):
    print(f"worker started for order {payload.order_id}")
    time.sleep(1)
    print(f"worker done for order {payload.order_id}")
    return True