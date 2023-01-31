import pynecone as pc


config = pc.Config(
    app_name="pynecone_practice",
    db_url="sqlite:///pynecone.db",
    env=pc.Env.DEV,
)
