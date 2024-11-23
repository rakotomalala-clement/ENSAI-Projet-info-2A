import unittest
import os
import pytest
from unittest.mock import patch
from utils.reset_database import ResetDatabase
from dao.dao_compte import DaoCompte
from business_object.utilisateur import Utilisateur


class TestDaoCompte(unittest.TestCase):
    """Classe de test pour vérifier le bon fonctionnement des méthodes de la classe DaoCompte."""

    def test_creer_utilisateur(self):
        """Test de la création d'un utilisateur dans la base de données."""

        utilisateur = Utilisateur(
            "testuser60",
            "testt",
        )
        creation_user = DaoCompte().creer_utilisateur(utilisateur)
        assert creation_user
        # Nettoyage : suppression de l'utilisateur ajouté pour éviter de polluer la base de données.
        suppression = DaoCompte().supprimer_utilisateur(utilisateur.id_utilisateur)
        assert suppression

    def test_trouver_utilisateur_par_id_true(self):
        """Test de la recherche d'un utilisateur par son identifiant (id)."""
        found_utilisateur = DaoCompte().trouver_utilisateur_par_id(16)
        assert found_utilisateur is not None

    def test_trouver_utilisateur_par_nom_true(self):
        """Test de la recherche d'un utilisateur par son nom d'utilisateur."""

        found_utilisateur = DaoCompte().trouver_utilisateur_par_nom("Lilian")
        assert found_utilisateur is not None

    def test_mettre_a_jour_utilisateur(self):
        """Test de la mise à jour des informations d'un utilisateur (nom et mot de passe)."""

        updated_utilisateur = DaoCompte().mettre_a_jour_utilisateur(
            49, "new_name", "new_password10"
        )
        assert updated_utilisateur

    def test_lister_tous(self):
        """Test de la récupération de la liste de tous les utilisateurs."""

        utilisateurs = DaoCompte().lister_tous()
        assert len(utilisateurs) == 30
        assert utilisateurs[0].nom_utilisateur == "test_user26"

    def test_supprimer_utilisateur(self):
        """Test de la suppression d'un utilisateur dans la base de données."""

        utilisateur = DaoCompte().trouver_utilisateur_par_id(65)
        assert utilisateur is not None
        result = DaoCompte().supprimer_utilisateur(65)
        assert result is True
        # Nettoyage : ajout d'un utilisateur après la suppression d'un autre pour maintenir l'execution des tests(le test lister_tous() vérifiant la longueur de la liste users).
        ajout = DaoCompte().creer_utilisateur(utilisateur)
        assert ajout


if __name__ == "__main__":
    unittest.main()
