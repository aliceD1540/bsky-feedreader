from js import Response


async def on_fetch(request, env):
    # CloudflareのD1 DBに接続
    db = env.get_db("d1_db")
    # testテーブルからレコード取得
    result = await db.query("SELECT * FROM test_tbl")
    # レスポンスを返す
    return Response.new(result)

    # return Response.new("Hello World!")
