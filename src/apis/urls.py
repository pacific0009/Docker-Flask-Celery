from apis import views


api_urls = [
    ("/", views.index, ["GET"], "flask scaffolding index url"),
    ("/login", views.login, ["POST"], "flask user login url")
]

other_urls = []

all_urls = api_urls + other_urls
