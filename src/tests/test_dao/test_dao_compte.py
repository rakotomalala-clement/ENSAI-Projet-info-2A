import unittest
import os
import pytest
from unittest.mock import patch
from utils.reset_database import ResetDatabase
from dao.dao_compte import DaoCompte
from business_object.utilisateur import Utilisateur


class TestDaoCompte(unittest.TestCase):
    def test_creer_utilisateur(self):
        utilisateur = Utilisateur("test_user2", "mdptest2")
        creation_user = DaoCompte().creer_utilisateur(utilisateur)
        assert creation_user

    def test_trouver_utilisateur_par_id_true(self):
        found_utilisateur = DaoCompte().trouver_utilisateur_par_id(1)
        assert found_utilisateur is not None

    def test_trouver_utilisateur_par_nom_true(self):
        found_utilisateur = DaoCompte().trouver_utilisateur_par_nom("nom1")
        assert found_utilisateur is not None

    def test_mettre_a_jour_utilisateur(self):
        # Test updating a user
        updated_utilisateur = DaoCompte().mettre_a_jour_utilisateur(1, "new_name", "new_password")
        assert updated_utilisateur

    def test_supprimer_utilisateur(self):
        # Test deleting a user

        result = DaoCompte().supprimer_utilisateur(utilisateur.id)
        self.assertTrue(result)
        self.assertIsNone(DaoCompte().trouver_utilisateur_par_id(utilisateur.id))

    """def tearDown(self):
        # Close connections or clean up database if necessary
        DaoCompte().fermer_connexion()"""


if __name__ == "__main__":
    unittest.main()
