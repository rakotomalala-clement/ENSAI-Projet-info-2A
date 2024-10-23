import unittest
import os
import pytest
from unittest.mock import patch
from utils.reset_database import ResetDatabase
from dao.dao_compte import DaoCompte
from business_object.utilisateur import Utilisateur


class TestDaoCompte(unittest.TestCase):
    def test_creer_utilisateur(self):
        utilisateur = Utilisateur("test_user5", "mdptest5")
        creation_user = DaoCompte().creer_utilisateur(utilisateur)
        assert creation_user

    def test_trouver_utilisateur_par_id_true(self):
        found_utilisateur = DaoCompte().trouver_utilisateur_par_id(10)
        assert found_utilisateur is not None

    def test_trouver_utilisateur_par_nom_true(self):
        found_utilisateur = DaoCompte().trouver_utilisateur_par_nom("test_user1")
        assert found_utilisateur is not None

    def test_mettre_a_jour_utilisateur(self):
        # Test updating a user
        updated_utilisateur = DaoCompte().mettre_a_jour_utilisateur(
            14, "new_name1", "new_password1"
        )
        assert updated_utilisateur

    def test_supprimer_utilisateur(self):
        # Test deleting a user

        result = DaoCompte().supprimer_utilisateur(15)
        self.assertTrue(result)

    """def tearDown(self):
        # Close connections or clean up database if necessary
        DaoCompte().fermer_connexion()"""


if __name__ == "__main__":
    unittest.main()
