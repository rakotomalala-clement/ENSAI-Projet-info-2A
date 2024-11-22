import logging.config
import logging
import numbers

from functools import wraps


class LogIndetation:
    current_indentation = 0

    @classmethod
    def increase_indentation(cls):
        cls.current_indentation += 1

    @classmethod
    def decrease_indentation(cls):
        cls.current_indentation -= 1

    @classmethod
    def get_indentation(cls):
        return "    " * cls.current_indentation


def log(func):
    """Création d'un décorateur nommé log
    Lorsque ce décorateur est appliqué à une méthode, cela affichera dans les logs :
    * l'appel de cette méthode avec les valeurs de paramètres
    * la sortie retournée par cette méthode
    """

    @wraps(func)
    def wrapper(*args, **kwargs):
        logger = logging.getLogger(__name__)

        LogIndetation.increase_indentation()
        indentation = LogIndetation.get_indentation()

        class_name = args[0].__class__.__name__ if args else ""
        method_name = func.__name__
        args_list = tuple(
            [str(arg) if not isinstance(arg, numbers.Number) else arg for arg in args[1:]]
        )

        logger.info(f"{indentation}{class_name}.{method_name}{args_list} - DEBUT")

        result = func(*args, **kwargs)

        logger.info(f"{indentation}{class_name}.{method_name}{args_list} - FIN")

        if isinstance(result, list):
            result_str = str([str(item) for item in result[:3]])
            result_str += " ... (" + str(len(result)) + " elements)"
        elif isinstance(result, dict):
            result_str = [(str(k), str(v)) for k, v in result.items()][:3]
            result_str += " ... (" + str(len(result)) + " elements)"
        else:
            result_str = str(result)

        logger.info(f"{indentation}   └─> Sortie : {result_str}")

        LogIndetation.decrease_indentation()

        return result

    return wrapper
