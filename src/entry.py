from js import Response


async def on_fetch(request, env):
    # CloudflareのD1 DBに接続
    stmt = env.DB.prepare("SELECT * FROM test_tbl")

    result = await stmt.all()

    # レスポンスを返す
    return Response.new(result)

    # return Response.new("Hello World!")
