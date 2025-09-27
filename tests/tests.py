import unittest
from unittest.mock import MagicMock, patch


class TestSecretaryInitialization(unittest.TestCase):
    
    def test_secretary_gets_email_on_initialization(self):
        """Test that every secretary gets an email address when initialized."""
        # Import Secretary class (assuming it will be in src)
        # from src.secretary import Secretary
        
        # For now, we'll create a mock test that demonstrates the expected behavior
        # When Secretary class is implemented, remove the mock and use actual import
        
        # Mock the Secretary class
        Secretary = MagicMock()
        
        # Create test instances
        test_emails = [
            "john.doe@company.com",
            "jane.smith@company.com", 
            "bob.wilson@company.com"
        ]
        
        test_names = ["John Doe", "Jane Smith", "Bob Wilson"]
        
        # Test that each secretary gets initialized with an email
        for name, email in zip(test_names, test_emails):
            # When Secretary class is implemented, this would be:
            # secretary = Secretary(name=name, email=email)
            secretary = Secretary(name=name, email=email)
            
            # Assert that the secretary has an email attribute
            self.assertIsNotNone(secretary.email)
            self.assertEqual(secretary.email, email)
            
        # Test that secretary cannot be created without email
        with self.assertRaises(TypeError):
            # When implemented, this should raise TypeError for missing required email
            Secretary(name="No Email Person")


if __name__ == '__main__':
    unittest.main()