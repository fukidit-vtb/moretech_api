from api.v1.base import api_v1_router
from api.v1.schemas.search import SearchByParams, SearchByParamsOut


@api_v1_router.post('/search_by_params')
async def search_by_params(
    params: SearchByParams,
) -> SearchByParamsOut:
    return SearchByParamsOut(
        items=[{'some': 'news'}],
        params=params,
    )
