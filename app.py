from fastapi import FastAPI
from starlette.responses import RedirectResponse

from settings import SERVICE_NAME

application = FastAPI(
    title=SERVICE_NAME,
    openapi_url="/api/openapi.json"
)


@application.get('/ping')
async def ping() -> str:
    return 'pong'


@application.get('/', include_in_schema=False)
async def redirect_to_docs() -> RedirectResponse:
    response = RedirectResponse(url='/docs')
    return response


def build_app() -> FastAPI:
    from api.v1.base import api_v1_router

    # include routers
    application.include_router(api_v1_router)

    return application
