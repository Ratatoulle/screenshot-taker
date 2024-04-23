from selenium_work.url.helper import make_valid_name
from selenium_work import screenshot
from minio_work.helper import MinioHelper
from database.helper import DBHelper
from fastapi import FastAPI, Depends, status, Response
from fastapi.responses import StreamingResponse
from pydantic import create_model
import uvicorn

app = FastAPI()

query_params = {"url": (str, "example.com"),
                "is_fresh": (bool, False)}

query_model = create_model("Query", **query_params)


@app.get("/take_from")
def take_from(request: query_model = Depends()):
    params = request.dict()
    url = params["url"]
    filename = make_valid_name(url) + ".png"
    if not params["is_fresh"]:
        helper = MinioHelper()
        image = helper.get_from(filename)
        if image:
            return StreamingResponse(image, media_type="image/png")
        else:
            return Response(status_code=status.HTTP_400_BAD_REQUEST)
    minio_helper = MinioHelper()
    db_helper = DBHelper()

    image_bytes = screenshot.take_from(url, sleep_time=5)

    if not image_bytes:
        return Response(status_code=status.HTTP_400_BAD_REQUEST)

    minio_helper.save_to(filename, image_bytes)
    minio_path = minio_helper.bucket_name + "/" + filename

    db_helper.add_link(url, minio_path)

    return status.HTTP_200_OK


def main():
    minio_helper = MinioHelper()
    db_helper = DBHelper()
    uvicorn.run(app, host="0.0.0.0", port=80)


if __name__ == "__main__":
    main()
