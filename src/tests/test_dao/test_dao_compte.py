import unittest
import os
import pytest
from unittest.mock import patch
from utils.reset_database import ResetDatabase
from dao.dao_compte import DaoCompte
from business_object.utilisateur import Utilisateur


class TestDaoCompte(unittest.TestCase):
    def test_creer_utilisateur(self):
        utilisateur = Utilisateur("test_user85", "mdptest85")
        creation_user = DaoCompte().creer_utilisateur(utilisateur)
        assert creation_user
        suppression = DaoCompte().supprimer_utilisateur(utilisateur.id_utilisateur)
        assert suppression

    def test_trouver_utilisateur_par_id_true(self):
        found_utilisateur = DaoCompte().trouver_utilisateur_par_id(16)
        assert found_utilisateur is not None

    def test_trouver_utilisateur_par_nom_true(self):
        found_utilisateur = DaoCompte().trouver_utilisateur_par_nom("Lilian")
        assert found_utilisateur is not None

    def test_mettre_a_jour_utilisateur(self):
        updated_utilisateur = DaoCompte().mettre_a_jour_utilisateur(
            42, "new_name20", "new_password110"
        )
        assert updated_utilisateur

    def test_lister_tous(self):
        utilisateurs = DaoCompte().lister_tous()
        assert len(utilisateurs) == 21
        assert utilisateurs[0].nom_utilisateur == "test_user26"

    def test_supprimer_utilisateur(self):
        utilisateur = DaoCompte().trouver_utilisateur_par_id(58)
        assert utilisateur is not None
        result = DaoCompte().supprimer_utilisateur(58)
        assert result is True
        ajout = DaoCompte().creer_utilisateur(utilisateur)
        assert ajout


"""def tearDown(self):
        # Close connections or clean up database if necessary
        DaoCompte().fermer_connexion()"""


if __name__ == "__main__":
    unittest.main()
