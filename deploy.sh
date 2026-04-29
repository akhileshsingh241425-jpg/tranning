#!/bin/bash
# TrainingProtec Deployment Script
# Usage: bash deploy.sh
# This script pulls latest code, rebuilds frontend, and restarts all services

set -e

echo "=========================================="
echo "  TrainingProtec Deployment Script"
echo "=========================================="

# Color codes
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
NC='\033[0m' # No Color

# Step 1: Pull latest code
echo -e "\n${YELLOW}[1/6] Pulling latest code from Git...${NC}"
cd /var/www/tranning
git pull origin master
echo -e "${GREEN}✓ Code pulled successfully${NC}"

# Step 2: Install/update Python dependencies
echo -e "\n${YELLOW}[2/6] Updating Python dependencies...${NC}"
cd /var/www/tranning/backend
source venv/bin/activate
pip install -r requirements.txt -q
echo -e "${GREEN}✓ Python dependencies updated${NC}"

# Step 3: Rebuild React frontend
echo -e "\n${YELLOW}[3/6] Building React frontend...${NC}"
cd /var/www/tranning
npm install --legacy-peer-deps
npm run build
echo -e "${GREEN}✓ Frontend built successfully${NC}"

# Step 4: Ensure upload folder permissions
echo -e "\n${YELLOW}[4/6] Setting file permissions...${NC}"
chown -R www-data:www-data /var/www/tranning/backend/static/uploads
chown -R www-data:www-data /var/www/tranning/build
echo -e "${GREEN}✓ Permissions set${NC}"

# Step 5: Restart Gunicorn (systemd service)
echo -e "\n${YELLOW}[5/6] Restarting Gunicorn...${NC}"
sudo systemctl restart gunicorn
sleep 2
if sudo systemctl is-active --quiet gunicorn; then
    echo -e "${GREEN}✓ Gunicorn is running${NC}"
else
    echo -e "${RED}✗ Gunicorn failed to start! Check logs:${NC}"
    sudo journalctl -u gunicorn -n 20 --no-pager
    exit 1
fi

# Step 6: Reload Nginx
echo -e "\n${YELLOW}[6/6] Reloading Nginx...${NC}"
sudo systemctl reload nginx
echo -e "${GREEN}✓ Nginx reloaded${NC}"

# Done
echo -e "\n${GREEN}=========================================="
echo -e "  Deployment Complete! 🚀"
echo -e "==========================================${NC}"
echo ""
echo "Useful commands:"
echo "  sudo systemctl status gunicorn   - Check backend status"
echo "  sudo systemctl restart gunicorn  - Restart backend"
echo "  sudo systemctl stop gunicorn     - Stop backend"
echo "  sudo journalctl -u gunicorn -f   - View live logs"
echo "  sudo tail -f /var/log/gunicorn/error.log - View error log"
