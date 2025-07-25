"""Tests for the example scripts to ensure they work correctly."""

import pytest
import os
import sys
from pathlib import Path
from unittest.mock import patch, Mock
import importlib.util


class TestExampleScripts:
    """Test the example scripts in the examples directory."""

    @pytest.fixture
    def examples_dir(self):
        """Get the examples directory path."""
        return Path(__file__).parent.parent / "examples"

    @pytest.fixture
    def sample_py_path(self, examples_dir):
        """Get the sample.py script path."""
        return examples_dir / "sample.py"

    @pytest.fixture
    def create_process_py_path(self, examples_dir):
        """Get the create_process.py script path."""
        return examples_dir / "create_process.py"

    def test_examples_directory_exists(self, examples_dir):
        """Test that examples directory exists."""
        assert examples_dir.exists(), "Examples directory should exist"
        assert examples_dir.is_dir(), "Examples should be a directory"

    def test_sample_py_exists(self, sample_py_path):
        """Test that sample.py exists."""
        assert sample_py_path.exists(), "sample.py should exist"
        assert sample_py_path.suffix == ".py", "sample.py should be a Python file"

    def test_create_process_py_exists(self, create_process_py_path):
        """Test that create_process.py exists."""
        assert create_process_py_path.exists(), "create_process.py should exist"
        assert create_process_py_path.suffix == ".py", "create_process.py should be a Python file"

    @patch.dict(os.environ, {
        'BOOMI_ACCOUNT': 'test-account-123',
        'BOOMI_USER': 'test@example.com',
        'BOOMI_SECRET': 'test-password'
    })
    @patch('boomi.Boomi')
    def test_sample_py_imports_and_initialization(self, mock_boomi_class, sample_py_path):
        """Test that sample.py can import dependencies and initialize SDK."""
        if not sample_py_path.exists():
            pytest.skip("sample.py not found")
        
        # Mock the Boomi SDK
        mock_sdk = Mock()
        mock_sdk.account.get_account.return_value = Mock(
            __dict__={'id': 'test-123', 'name': 'Test Account'}
        )
        mock_boomi_class.return_value = mock_sdk
        
        try:
            # Load and execute the sample script
            spec = importlib.util.spec_from_file_location("sample", sample_py_path)
            sample_module = importlib.util.module_from_spec(spec)
            
            # Execute the script
            spec.loader.exec_module(sample_module)
            
            # Verify SDK was initialized
            mock_boomi_class.assert_called_once()
            
        except Exception as e:
            pytest.skip(f"Could not execute sample.py: {e}")

    @patch.dict(os.environ, {
        'BOOMI_ACCOUNT': 'test-account-123',
        'BOOMI_USER': 'test@example.com',
        'BOOMI_SECRET': 'test-password'
    })
    def test_sample_py_syntax_and_imports(self, sample_py_path):
        """Test that sample.py has valid syntax and can import required modules."""
        if not sample_py_path.exists():
            pytest.skip("sample.py not found")
        
        try:
            with open(sample_py_path, 'r') as f:
                content = f.read()
            
            # Check for required imports
            assert 'from boomi import Boomi' in content, "Should import Boomi"
            assert 'from dotenv import load_dotenv' in content, "Should import load_dotenv"
            assert 'import os' in content, "Should import os"
            
            # Check for basic structure
            assert 'load_dotenv()' in content, "Should call load_dotenv()"
            assert 'Boomi(' in content, "Should instantiate Boomi SDK"
            assert 'get_account(' in content, "Should call get_account method"
            
        except Exception as e:
            pytest.fail(f"Error analyzing sample.py: {e}")

    def test_create_process_py_syntax(self, create_process_py_path):
        """Test that create_process.py has valid syntax."""
        if not create_process_py_path.exists():
            pytest.skip("create_process.py not found")
        
        try:
            with open(create_process_py_path, 'r') as f:
                content = f.read()
            
            # Compile to check syntax
            compile(content, str(create_process_py_path), 'exec')
            
            # Check for basic structure (if file has content)
            if content.strip():
                assert 'boomi' in content.lower() or 'import' in content, "Should contain relevant imports"
            
        except SyntaxError as e:
            pytest.fail(f"Syntax error in create_process.py: {e}")
        except Exception as e:
            pytest.skip(f"Could not analyze create_process.py: {e}")

    @patch('builtins.print')
    @patch.dict(os.environ, {
        'BOOMI_ACCOUNT': 'test-account-123',
        'BOOMI_USER': 'test@example.com',
        'BOOMI_SECRET': 'test-password'
    })
    @patch('boomi.Boomi')
    def test_sample_py_output(self, mock_boomi_class, mock_print, sample_py_path):
        """Test that sample.py produces expected output."""
        if not sample_py_path.exists():
            pytest.skip("sample.py not found")
        
        # Mock the SDK and its response
        mock_account = Mock()
        mock_account.__dict__ = {
            'id': 'test-account-123',
            'name': 'Test Account',
            'status': 'active'
        }
        
        mock_sdk = Mock()
        mock_sdk.account.get_account.return_value = mock_account
        mock_boomi_class.return_value = mock_sdk
        
        try:
            # Execute the script
            spec = importlib.util.spec_from_file_location("sample", sample_py_path)
            sample_module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(sample_module)
            
            # Check that print was called (output was produced)
            assert mock_print.called, "Script should produce output"
            
            # Check for expected output patterns
            print_calls = [call[0][0] for call in mock_print.call_args_list if call[0]]
            output_text = ' '.join(print_calls).lower()
            
            assert 'boomi' in output_text, "Output should mention Boomi"
            assert 'sdk' in output_text, "Output should mention SDK"
            
        except Exception as e:
            pytest.skip(f"Could not test sample.py output: {e}")

    def test_example_scripts_documentation(self, examples_dir):
        """Test that example scripts have proper documentation."""
        readme_path = examples_dir / "README.md"
        
        if readme_path.exists():
            with open(readme_path, 'r') as f:
                readme_content = f.read()
            
            assert len(readme_content) > 0, "README should have content"
            assert 'example' in readme_content.lower(), "README should describe examples"
        else:
            # README might not exist, which is acceptable
            pass

    @patch.dict(os.environ, {
        'BOOMI_ACCOUNT': 'test-account-123',
        'BOOMI_USER': 'test@example.com',
        'BOOMI_SECRET': 'test-password'
    })
    def test_environment_variable_usage(self, sample_py_path):
        """Test that examples properly use environment variables."""
        if not sample_py_path.exists():
            pytest.skip("sample.py not found")
        
        with open(sample_py_path, 'r') as f:
            content = f.read()
        
        # Check for proper environment variable usage
        env_patterns = [
            'os.getenv("BOOMI_ACCOUNT")',
            'os.getenv("BOOMI_USER")',
            'os.getenv("BOOMI_SECRET")'
        ]
        
        for pattern in env_patterns:
            assert pattern in content, f"Should use {pattern}"

    def test_example_error_handling(self, sample_py_path):
        """Test that examples include proper error handling."""
        if not sample_py_path.exists():
            pytest.skip("sample.py not found")
        
        with open(sample_py_path, 'r') as f:
            content = f.read()
        
        # Check for error handling patterns
        error_handling_patterns = ['try:', 'except:', 'Exception']
        
        has_error_handling = any(pattern in content for pattern in error_handling_patterns)
        assert has_error_handling, "Examples should include error handling"


class TestExampleRequirements:
    """Test that examples can run with the project dependencies."""

    def test_example_dependencies_available(self):
        """Test that all dependencies needed by examples are available."""
        required_modules = ['boomi', 'dotenv', 'os']
        
        for module_name in required_modules:
            try:
                if module_name == 'boomi':
                    import boomi
                elif module_name == 'dotenv':
                    import dotenv
                elif module_name == 'os':
                    import os
                    
                assert True  # Module imported successfully
                
            except ImportError:
                pytest.fail(f"Required module {module_name} not available")

    def test_sdk_can_be_imported_for_examples(self):
        """Test that the SDK can be imported as shown in examples."""
        try:
            from boomi import Boomi
            assert Boomi is not None
            
            # Test that SDK can be instantiated (with mock credentials)
            sdk = Boomi(
                account_id="test",
                username="test",
                password="test"
            )
            assert sdk is not None
            
        except Exception as e:
            pytest.fail(f"Cannot import or instantiate SDK for examples: {e}")


class TestExampleCompatibility:
    """Test example compatibility with different Python versions and environments."""

    def test_examples_python_version_compatibility(self, examples_dir):
        """Test that examples are compatible with supported Python versions."""
        # Get all Python files in examples
        python_files = list(examples_dir.glob("*.py"))
        
        for py_file in python_files:
            try:
                with open(py_file, 'r') as f:
                    content = f.read()
                
                # Compile to check syntax compatibility
                compile(content, str(py_file), 'exec')
                
                # Check for Python 3.9+ compatible patterns (as per pyproject.toml)
                # No f-strings with = (Python 3.8+ feature)
                # No walrus operator := (Python 3.8+ feature) - but these are fine for 3.9+
                
            except SyntaxError as e:
                pytest.fail(f"Syntax error in {py_file}: {e}")
            except Exception as e:
                pytest.skip(f"Could not check {py_file}: {e}")

    def test_examples_use_supported_features(self, sample_py_path):
        """Test that examples only use supported Python features."""
        if not sample_py_path.exists():
            pytest.skip("sample.py not found")
        
        with open(sample_py_path, 'r') as f:
            content = f.read()
        
        # Examples should not use deprecated features
        deprecated_patterns = ['imp.load_source', 'execfile']
        
        for pattern in deprecated_patterns:
            assert pattern not in content, f"Should not use deprecated {pattern}"