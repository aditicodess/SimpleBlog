from drf_yasg import openapi


response200 = openapi.Response(
    "Success",
    schema=openapi.Schema(
        type=openapi.TYPE_OBJECT,
        properties={
            "User Registration": openapi.Schema(
                type=openapi.TYPE_OBJECT,
                default="User",
                properties={
                    "username": openapi.Schema(
                        type=openapi.TYPE_STRING,
                    ),
                    "password": openapi.Schema(
                        type=openapi.TYPE_STRING,
                    ),
                },
            )
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
