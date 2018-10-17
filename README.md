# host_info_fetcher
An utility for fetching some infomation about your host and the lan network.

Only support **windows** and works with python3.

# Install dependencies
```
pip install PyQt5 psutil pyinstaller
```

# Build executable binary for using without python interpreter
```
git clone https://github.com/ncu-electronic/host_info_fetcher
cd host_info_fetcher
pyinstaller -w -i icon.ico host_info_fetcher.py
```
You can run the generated binary `host_info_fetcher.exe` in the dist directory to start.

# Changelog
2018.10.17 - Add an option in systray menu to hide itself for five minutes.

# Screenshots
![screenshot_0](https://raw.githubusercontent.com/ncu-electronic/host_info_fetcher/master/screenshots/Snipaste_2018-09-15_17-13-58.png)
![screenshot_1](https://raw.githubusercontent.com/ncu-electronic/host_info_fetcher/master/screenshots/Snipaste_2018-09-15_17-14-16.png)
