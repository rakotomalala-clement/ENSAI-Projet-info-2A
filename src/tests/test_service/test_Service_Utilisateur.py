import unittest
import os
import pytest
from unittest.mock import patch
from utils.reset_database import ResetDatabase
from dao.dao_compte import DaoCompte
from business_object.utilisateur import Utilisateur
from service.Service_Utilisateur import ServiceUtilisateur


class TestServiceUtilisateur(unittest.TestCase):
    def tester_sinscrire():
        utilisateur = Utilisateur("test_user10", "mdptest")
        inscription_user = ServiceUtilisateur().sinscrire(utilisateur)
        assert inscription_user
