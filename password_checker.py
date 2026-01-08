import re
import hashlib
import requests
import string

class PasswordChecker:
    """
    Analyzes password strength using multiple criteria:
    - Length (8-16+ characters)
    - Complexity (uppercase, lowercase, numbers, symbols)
    - Pattern detection (common patterns, sequences)
    - Breach detection (using Have I Been Pwned API)
    - Dictionary words
    """
    
    def __init__(self):
        self.common_passwords = self.load_common_passwords()
        self.min_length = 8
        self.recommended_length = 12
        self.strong_length = 16
        
    def load_common_passwords(self):
        """Load list of commonly used weak passwords"""
        common = [
            'password', '123456', '12345678', 'qwerty', 'abc123',
            'monkey', '1234567', 'letmein', 'trustno1', 'dragon',
            'baseball', '111111', 'iloveyou', 'master', 'sunshine',
            'ashley', 'bailey', 'passw0rd', 'shadow', '123123',
            '654321', 'superman', 'qazwsx', 'michael', 'football',
            'admin', 'login', 'pass', 'test', 'guest',
            'welcome', 'hello', 'hello123', 'admin123', 'root',
            'toor', 'user', 'pass123', '123', 'password123'
        ]
        return common
    
    def get_common_passwords(self):
        """Return list of common passwords"""
        return self.common_passwords
    
    def check_strength(self, password):
        """
        Main method to check password strength
        Returns dictionary with score, strength level, and feedback
        """
        score = 0
        feedback = []
        issues = []
        
        # 1. Length Check (0-25 points)
        length_score = self.check_length(password)
        score += length_score[0]
        if length_score[1]:
            feedback.append(length_score[1])
        if length_score[2]:
            issues.append(length_score[2])
        
        # 2. Complexity Check (0-25 points)
        complexity_score = self.check_complexity(password)
        score += complexity_score[0]
        for item in complexity_score[1]:
            feedback.append(item)
        for item in complexity_score[2]:
            issues.append(item)
        
        # 3. Pattern Detection (0-20 points)
        pattern_score = self.check_patterns(password)
        score += pattern_score[0]
        for item in pattern_score[1]:
            feedback.append(item)
        for item in pattern_score[2]:
            issues.append(item)
        
        # 4. Dictionary Words Check (0-15 points)
        dict_score = self.check_dictionary(password)
        score += dict_score[0]
        if dict_score[1]:
            feedback.append(dict_score[1])
        if dict_score[2]:
            issues.append(dict_score[2])
        
        # 5. Entropy Check (0-15 points)
        entropy_score = self.check_entropy(password)
        score += entropy_score[0]
        if entropy_score[1]:
            feedback.append(entropy_score[1])
        
        # Cap score at 100
        score = min(score, 100)
        
        # Determine strength level
        if score >= 80:
            strength = 'Very Strong'
            strength_level = 5
        elif score >= 60:
            strength = 'Strong'
            strength_level = 4
        elif score >= 40:
            strength = 'Good'
            strength_level = 3
        elif score >= 20:
            strength = 'Weak'
            strength_level = 2
        else:
            strength = 'Very Weak'
            strength_level = 1
        
        return {
            'score': score,
            'strength': strength,
            'strength_level': strength_level,
            'feedback': feedback,
            'issues': issues,
            'message': self.get_message(score)
        }
    
    def check_length(self, password):
        """Check password length"""
        length = len(password)
        points = 0
        feedback = ""
        issue = ""
        
        if length < self.min_length:
            points = 5
            issue = f"Password is too short (min {self.min_length} characters)"
        elif length < self.recommended_length:
            points = 15
            feedback = f"Consider using at least {self.recommended_length} characters"
        elif length < self.strong_length:
            points = 20
            feedback = "Length is good. Consider making it even longer"
        else:
            points = 25
            feedback = "Excellent length!"
        
        return (points, feedback, issue)
    
    def check_complexity(self, password):
        """Check character complexity"""
        points = 0
        feedback = []
        issues = []
        
        has_upper = bool(re.search(r'[A-Z]', password))
        has_lower = bool(re.search(r'[a-z]', password))
        has_digit = bool(re.search(r'[0-9]', password))
        has_symbol = bool(re.search(r'[!@#$%^&*()_+\-=\[\]{};:\'",.<>?/\\|`~]', password))
        
        complexity_count = sum([has_upper, has_lower, has_digit, has_symbol])
        
        # Award points based on complexity
        if has_upper:
            points += 5
            feedback.append("✓ Contains uppercase letters")
        else:
            issues.append("Missing uppercase letters")
        
        if has_lower:
            points += 5
            feedback.append("✓ Contains lowercase letters")
        else:
            issues.append("Missing lowercase letters")
        
        if has_digit:
            points += 5
            feedback.append("✓ Contains numbers")
        else:
            issues.append("Missing numbers")
        
        if has_symbol:
            points += 10
            feedback.append("✓ Contains special symbols")
        else:
            issues.append("No special symbols used")
        
        return (points, feedback, issues)
    
    def check_patterns(self, password):
        """Detect common patterns"""
        points = 0
        feedback = []
        issues = []
        
        # Check for sequences
        has_sequential = bool(re.search(r'(012|123|234|345|456|567|678|789|890|abc|bcd|cde|def)', password.lower()))
        has_repeated = bool(re.search(r'(.)\1{2,}', password))  # 3+ repeated chars
        
        if not has_sequential:
            points += 10
            feedback.append("✓ No sequential characters detected")
        else:
            issues.append("Contains sequential characters (e.g., 123, abc)")
        
        if not has_repeated:
            points += 10
            feedback.append("✓ No repeated characters detected")
        else:
            issues.append("Contains repeated characters")
        
        return (points, feedback, issues)
    
    def check_dictionary(self, password):
        """Check against common passwords and dictionary words"""
        points = 15
        feedback = ""
        issue = ""
        
        password_lower = password.lower()
        
        # Check common passwords
        if password_lower in self.common_passwords:
            points = 0
            issue = "This is a very common password"
            return (points, feedback, issue)
        
        # Check if password contains common words
        for common in self.common_passwords:
            if common in password_lower and len(common) > 3:
                points = 5
                issue = f"Contains common word: '{common}'"
                return (points, feedback, issue)
        
        feedback = "✓ Not in common password database"
        return (points, feedback, "")
    
    def check_entropy(self, password):
        """Calculate password entropy"""
        points = 0
        feedback = ""
        
        # Estimate character set size
        charset_size = 0
        if re.search(r'[a-z]', password):
            charset_size += 26
        if re.search(r'[A-Z]', password):
            charset_size += 26
        if re.search(r'[0-9]', password):
            charset_size += 10
        if re.search(r'[^a-zA-Z0-9]', password):
            charset_size += 32
        
        # Calculate entropy
        import math
        if charset_size > 0:
            entropy = len(password) * math.log2(charset_size)
            
            if entropy >= 50:
                points = 15
                feedback = f"✓ High entropy ({entropy:.1f} bits)"
            elif entropy >= 30:
                points = 10
                feedback = f"Good entropy ({entropy:.1f} bits)"
            else:
                points = 5
                feedback = f"Low entropy ({entropy:.1f} bits)"
        
        return (points, feedback)
    
    def check_breach(self, password):
        """
        Check if password has been breached using Have I Been Pwned API
        Uses k-anonymity: only sends first 5 chars of SHA-1 hash
        """
        try:
            # Hash the password with SHA-1
            sha1_hash = hashlib.sha1(password.encode()).hexdigest().upper()
            
            # Send only the first 5 characters
            prefix = sha1_hash[:5]
            suffix = sha1_hash[5:]
            
            # Query the HIBP API (k-anonymity model)
            response = requests.get(
                f'https://api.pwnedpasswords.com/range/{prefix}',
                timeout=5,
                headers={'User-Agent': 'PasswordStrengthAnalyzer'}
            )
            
            if response.status_code == 200:
                # Check if our hash suffix is in the response
                hashes = response.text.split('\r\n')
                for hash_line in hashes:
                    parts = hash_line.split(':')
                    if parts[0] == suffix:
                        return True  # Password has been breached
                return False
            else:
                return False  # Can't check, assume safe
                
        except Exception as e:
            print(f"Error checking breach database: {e}")
            return False  # Can't check, assume safe
    
    def get_message(self, score):
        """Get recommendation message based on score"""
        if score >= 80:
            return "Excellent! This is a very secure password."
        elif score >= 60:
            return "Good password. Consider the suggestions above to make it stronger."
        elif score >= 40:
            return "Moderate password. Follow the feedback to improve security."
        elif score >= 20:
            return "Weak password. Please address the issues listed above."
        else:
            return "Very weak password. Please create a much stronger one."
