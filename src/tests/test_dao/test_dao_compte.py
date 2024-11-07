import unittest
import os
import pytest
from unittest.mock import patch
from utils.reset_database import ResetDatabase
from dao.dao_compte import DaoCompte
from business_object.utilisateur import Utilisateur


class TestDaoCompte(unittest.TestCase):
    def test_creer_utilisateur(self):
        utilisateur = Utilisateur("test_user33", "mdptest32")
        print("************")
        creation_user = DaoCompte().creer_utilisateur(utilisateur)
        assert creation_user

    def test_trouver_utilisateur_par_id_true(self):
        found_utilisateur = DaoCompte().trouver_utilisateur_par_id(12)
        assert found_utilisateur is not None

    def test_trouver_utilisateur_par_nom_true(self):
        found_utilisateur = DaoCompte().trouver_utilisateur_par_nom("Lilian")
        assert found_utilisateur is not None

    def test_mettre_a_jour_utilisateur(self):
        # Test updating a user
        updated_utilisateur = DaoCompte().mettre_a_jour_utilisateur(
            37, "new_name15", "new_password15"
        )
        assert updated_utilisateur

    def test_lister_tous(self):
        utilisateurs = DaoCompte().lister_tous()

        # Assertions
        assert len(utilisateurs) == 15
        assert utilisateurs[0].nom_utilisateur == "test_user25"

    def test_supprimer_utilisateur(self):
        # Test deleting a user
        result = DaoCompte().supprimer_utilisateur(37)
        assert result is True


"""def tearDown(self):
        # Close connections or clean up database if necessary
        DaoCompte().fermer_connexion()"""


if __name__ == "__main__":
    unittest.main()
