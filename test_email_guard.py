import unittest
import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from ai.email_guard import classify_email

class TestEmailGuard(unittest.TestCase):

    def test_legit_email(self):
        """
        Test case for a legitimate (non-spam/non-phishing) email.
        Expected: 'legit' classification.
        """
        email_text = "Hi team, just a reminder about our meeting tomorrow at 10 AM. See you there."
        result = classify_email(email_text)

        self.assertIsInstance(result, dict)
        self.assertIn('classification', result)
        self.assertIn('confidence', result)
        self.assertIn('explanation', result)

        self.assertEqual(result['classification'], 'legit')
        self.assertGreaterEqual(result['confidence'], 0.0)
        self.assertLessEqual(result['confidence'], 1.0)
        self.assertIsInstance(result['explanation'], str)
        self.assertIn('LABEL_0', result['explanation']) 

    def test_spam_email(self):
        """
        Test case for a typical spam email.
        Expected: 'spam' classification.
        """
        
        email_text = "Free entry in to weekly competition to win a £100. Text 'WIN' to 80085 now!"
        result = classify_email(email_text)

        self.assertIsInstance(result, dict)
        self.assertIn('classification', result)
        self.assertIn('confidence', result)
        self.assertIn('explanation', result)

        self.assertEqual(result['classification'], 'spam')
        self.assertGreaterEqual(result['confidence'], 0.0)
        self.assertLessEqual(result['confidence'], 1.0)
        self.assertIsInstance(result['explanation'], str)
        self.assertIn('LABEL_1', result['explanation']) 

    def test_phishing_email(self):
        """
        Test case for a phishing email.
        Expected: 'spam' classification (as per model's current behavior for phishing).
        """
        email_text = """
        Subject: Urgent Security Alert: Your Apple ID Has Been Locked
        Dear Customer,
        Your Apple ID has been temporarily locked due to unusual activity.
        To unlock your account, click: http://verify-apple-account.malicious-site.com/login
        Apple Support
        """
        result = classify_email(email_text)

        self.assertIsInstance(result, dict)
        self.assertIn('classification', result)
        self.assertIn('confidence', result)
        self.assertIn('explanation', result)

       
        self.assertEqual(result['classification'], 'spam')
        self.assertGreaterEqual(result['confidence'], 0.0)
        self.assertLessEqual(result['confidence'], 1.0)
        self.assertIsInstance(result['explanation'], str)
        self.assertIn('LABEL_1', result['explanation'])


    def test_empty_input(self):
        """
        Test case for empty string input.
        Expected: 'legit' for empty input as it's not spam/malicious.
        """
        email_text = ""
        result = classify_email(email_text)

        self.assertIsInstance(result, dict)
        self.assertIn('classification', result)
        self.assertIn('confidence', result)
        self.assertIn('explanation', result)
        self.assertEqual(result['classification'], 'legit') 

    def test_very_long_input(self):
        """
        Test case for very long input to check if it's handled without error (due to truncation).
        """
        long_text = "This is a long sentence. " * 500 
        result = classify_email(long_text)

        self.assertIsInstance(result, dict)
        self.assertIn('classification', result)
        
        self.assertIn(result['classification'], ['legit', 'spam'])
        self.assertGreaterEqual(result['confidence'], 0.0)
        self.assertLessEqual(result['confidence'], 1.0)

if __name__ == '__main__':
    unittest.main()