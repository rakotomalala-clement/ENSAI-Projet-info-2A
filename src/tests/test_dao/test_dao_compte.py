import unittest
import os
import pytest
from unittest.mock import patch
from utils.reset_database import ResetDatabase
from dao.dao_compte import DaoCompte
from business_object.utilisateur import Utilisateur


class TestDaoCompte(unittest.TestCase):
    def test_creer_utilisateur():
        utilisateur = Utilisateur("test_user", "mdptest")
        creation_user = DaoCompte().creer_utilisateur(utilisateur)
        assert creation_user

    def test_trouver_utilisateur_par_id_true():
        found_utilisateur = DaoCompte().trouver_utilisateur_par_id(3)
        assert found_utilisateur is not None

    def test_trouver_utilisateur_par_nom_true():
        found_utilisateur = DaoCompte().trouver_utilisateur_par_nom("test_user")
        assert found_utilisateur is not None

    def test_mettre_a_jour_utilisateur():
        # Test updating a user
        updated_utilisateur = DaoCompte().mettre_a_jour_utilisateur(3, "new_name", "new_password")
        assert updated_utilisateur

    def test_supprimer_utilisateur():
        # Test deleting a user
        utilisateur = DaoCompte().creer_utilisateur("test_user", "password123")
        result = DaoCompte().supprimer_utilisateur(utilisateur.id)
        self.assertTrue(result)
        self.assertIsNone(DaoCompte().trouver_utilisateur_par_id(utilisateur.id))

    """def tearDown(self):
        # Close connections or clean up database if necessary
        DaoCompte().fermer_connexion()"""


if __name__ == "__main__":
    unittest.main()
