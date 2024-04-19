from selenium_work.url.helper import get_domen_name
from selenium_work.screenshot import ScreenshotTaker
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
         # responses={
         #     200: {
         #         "content": {"image/png": {}}
         #     }
         # },
         # response_class=Response)
def take_from(request: query_model = Depends()):
    params = request.dict()
    url = params["url"]
    filename = get_domen_name(url) + ".png"
    if not params["is_fresh"]:
        # image_bytes = get_image_bytes(filename)
        image = MinioHelper().get_from(filename)

        # if image:
        #     return Response(content=image, media_type="image/png")
        if image:
            return StreamingResponse(image, media_type="image/png")
        else:
            return Response(content="No such file on server, set is_fresh flag to True to make new screenshot.")
    # with ScreenshotTaker() as taker:
    minio_helper = MinioHelper()
    db_helper = DBHelper()

    image_bytes = screenshot.take_from(url, sleep_time=10)

    minio_helper.save_to(filename, image_bytes)
    minio_path = minio_helper.bucket_name + "/" + filename

    db_helper.add_link(url, minio_path)

    return status.HTTP_200_OK


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)