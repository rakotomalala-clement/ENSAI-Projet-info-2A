class Singleton(type):

    _instances = {}

    def __call__(cls, *args, **kwargs):
        """
        Si une instance est déjà créée, on la retourne. Sinon on en crée une nouvelle
        """
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]
