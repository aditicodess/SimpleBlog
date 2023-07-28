from drf_yasg import openapi

id_param_config = openapi.Parameter(
    "id",
    in_=openapi.IN_QUERY,
    description="Provide your post's id here",
    type=openapi.TYPE_STRING,
)
response200 = openapi.Response(
    "Success",
    schema=openapi.Schema(
        type=openapi.TYPE_OBJECT,
        properties={
            "Message": openapi.Schema(
                type=openapi.TYPE_OBJECT,
                properties={
                    "title": openapi.Schema(
                        type=openapi.TYPE_STRING, default="Programming"
                    ),
                    "description": openapi.Schema(
                        type=openapi.TYPE_STRING,
                        default="This is the description about the programming category of the blogs",
                    ),
                    "image": openapi.Schema(
                        type=openapi.TYPE_STRING,
                        default="This is the url of the image of the blogs",
                    ),
                },
            ),
            "Status": openapi.Schema(type=openapi.TYPE_INTEGER, default=200),
            "time": openapi.Schema(
                type=openapi.TYPE_STRING,
                default="TIME VALUE",
            ),
        },
    ),
)
response401 = openapi.Response(
    "Unauthorized response",
    schema=openapi.Schema(
        type=openapi.TYPE_OBJECT,
        properties={
            "Code": openapi.Schema(
                type=openapi.TYPE_STRING,
                default="AUTHENTICATION FAILED | NOT AUTHENTICATED",
            ),
            "Message": openapi.Schema(
                type=openapi.TYPE_STRING,
                default="INVALID_TOKEN | NOT AUTHENTICATED",
            ),
            "Status": openapi.Schema(type=openapi.TYPE_INTEGER, default=401),
            "time": openapi.Schema(
                type=openapi.TYPE_STRING,
                default="TIME VALUE",
            ),
        },
    ),
)
response404 = openapi.Response(
    "Page Not Found",
    schema=openapi.Schema(
        type=openapi.TYPE_OBJECT,
        properties={
            "Code": openapi.Schema(
                type=openapi.TYPE_STRING,
                default="Page_not_found",
            ),
            "Message": openapi.Schema(
                type=openapi.TYPE_STRING,
                default="PAGE NOT FOUND",
            ),
            "Status": openapi.Schema(type=openapi.TYPE_INTEGER, default=404),
            "time": openapi.Schema(
                type=openapi.TYPE_STRING,
                default="TIME VALUE",
            ),
        },
    ),
)

category_param_config = (
    openapi.Schema(
        type=openapi.TYPE_OBJECT,
        required=["title"],
        properties={
            "title": openapi.Schema(type=openapi.TYPE_STRING, default="Programming"),
            "description": openapi.Schema(
                type=openapi.TYPE_STRING,
                default="This is the description about the programming category of the blogs",
            ),
            "image": openapi.Schema(
                type=openapi.TYPE_STRING,
                default="This is the url of the image of the blogs",
            ),
        },
    ),
)
