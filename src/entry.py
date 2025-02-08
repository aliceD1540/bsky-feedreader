from js import Response


async def on_fetch(request, env):
    # CloudflareのD1 DBに接続
    # results = await env.DB.prepare("PRAGMA table_list").all()
    results = await env.DB.prepare("SELECT * FROM test_tbl").all()

    # レスポンスを返す
    return Response.new(results)

    # return Response.new("Hello World!")
