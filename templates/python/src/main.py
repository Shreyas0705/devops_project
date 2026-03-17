def handler(event=None, context=None):
    return {"message": "Hello from {{PROJECT_NAME}}"}


if __name__ == "__main__":
    print(handler())
