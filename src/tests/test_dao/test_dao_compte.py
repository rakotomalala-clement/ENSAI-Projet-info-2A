import unittest
from dao.dao_compte import DaoCompte
from dao.db_connection import DBConnection


class TestDaoCompte(unittest.TestCase):

    def test_creer_utilisateur():
        # Test the creation of a user
        utilisateur = DaoCompte().creer_utilisateur("test_user", "password123")
        assertIsNotNone(utilisateur)
        assertEqual(utilisateur.nom_utilisateur, "test_user")

    def test_trouver_utilisateur_par_id(self):
        # Test finding a user by ID
        utilisateur = DaoCompte().creer_utilisateur("test_user", "password123")
        found_utilisateur = DaoCompte().trouver_utilisateur_par_id(utilisateur.id)
        assertEqual(found_utilisateur.nom_utilisateur, "test_user")

    def test_trouver_utilisateur_par_nom(self):
        # Test finding a user by username
        DaoCompte().creer_utilisateur("test_user", "password123")
        found_utilisateur = DaoCompte().trouver_utilisateur_par_nom("test_user")
        assertIsNotNone(found_utilisateur)
        assertEqual(found_utilisateur.nom_utilisateur, "test_user")

    def test_mettre_a_jour_utilisateur(self):
        # Test updating a user
        utilisateur = DaoCompte().creer_utilisateur("test_user", "password123")
        updated_utilisateur = DaoCompte().mettre_a_jour_utilisateur(
            utilisateur.id, "new_name", "new_password"
        )
        assertEqual(updated_utilisateur.nom_utilisateur, "new_name")

    def test_supprimer_utilisateur(self):
        # Test deleting a user
        utilisateur = DaoCompte().creer_utilisateur("test_user", "password123")
        result = DaoCompte().supprimer_utilisateur(utilisateur.id)
        self.assertTrue(result)
        self.assertIsNone(DaoCompte().trouver_utilisateur_par_id(utilisateur.id))

    def tearDown(self):
        # Close connections or clean up database if necessary
        DaoCompte().fermer_connexion()


if __name__ == "__main__":
    unittest.main()
