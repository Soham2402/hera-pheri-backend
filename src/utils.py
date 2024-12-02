import importlib


async def get_database_dependency():
    main_module = importlib.import_module("src.main")
    return await main_module.get_database()
