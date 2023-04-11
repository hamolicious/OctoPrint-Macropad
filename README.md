## Setup
### systemd file
**location**: `/etc/systemd/system/`
**permission**: `sudo chmod 644 /etc/systemd/system/macropad.service`

```bash
sudo systemctl daemon-reload
sudo systemctl enable macropad.service
```
