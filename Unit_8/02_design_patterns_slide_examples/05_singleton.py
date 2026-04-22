
# Singleton
class AppConfig:
    _instance = None

    def __init__(self):
        self.values = {"database_url": "sqlite:///app.db"}

    @classmethod
    def get_instance(cls):
        if cls._instance is None:
            cls._instance = AppConfig()
        return cls._instance


def main():
    first = AppConfig.get_instance()
    second = AppConfig.get_instance()
    second.values["debug"] = True
    print(first is second, first.values)


if __name__ == "__main__":
    main()