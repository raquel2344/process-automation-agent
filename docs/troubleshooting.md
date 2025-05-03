# Troubleshooting

## Common Issues and Solutions

### 1. Installation Issues
- **Problem**: Dependencies fail to install.
- **Solution**: Ensure you have the correct Python version (`python --version`).
  ```bash
  pip install -r requirements.txt
  ```

### 2. API Errors
- **Problem**: Invalid API key.
- **Solution**: Verify the keys in the `.env` file.

### 3. Application Crashes
- **Problem**: Missing environment variables.
- **Solution**: Check if `.env` is properly configured.

### 4. Web Interface Not Loading
- **Problem**: Port conflict or server not running.
- **Solution**: Use an alternative port or debug the server:
  ```bash
  python src/main.py
  ```

### 5. Test Failures
- **Problem**: Unit tests fail due to missing dependencies.
- **Solution**: Reinstall dependencies and retry:
  ```bash
  pip install -r requirements.txt
  pytest
  ```

## Advanced Debugging
- Use logging to identify issues (`logs/` directory).
- Enable debug mode in Flask/FastAPI for detailed error messages.