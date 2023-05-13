### Eclipse-Oxygen
$ sudo apt update
$ wget -O eclipse.tar.gz "https://www.eclipse.org/downloads/download.php?file=/technology/epp/downloads/release/oxygen/3a/eclipse-jee-oxygen-3a-linux-gtk-x86_64.tar.gz&r=1"
$ tar -xzf eclipse.tar.gz
$ sudo mv eclipse /opt
$ sudo nano /usr/share/applications/eclipse.desktop

[Desktop Entry]
Name=Eclipse Oxygen
Type=Application
Exec=/opt/eclipse/eclipse
Terminal=false
Icon=/opt/eclipse/icon.xpm
Comment=Integrated Development Environment
NoDisplay=false
Categories=Development;IDE;
Name[en]=Eclipse

$ sudo chmod +x /usr/share/applications/eclipse.desktop

---
Dowload using snap
--
$ snap search eclipse


---
### Tomcat for Java 8
$ sudo apt update
$ sudo apt install openjdk-8-jdk
$ wget https://downloads.apache.org/tomcat/tomcat-8/v8.5.88/bin/apache-tomcat-8.5.88.tar.gz
$ tar -xf apache-tomcat-8.5.88.tar.gz
$ sudo mv apache-tomcat-8.5.88 /opt/tomcat
$ sudo chmod +x /opt/tomcat/bin/*.sh
$ sudo nano /etc/systemd/system/tomcat.service


[Unit]
Description=Apache Tomcat Web Application Container
After=network.target

[Service]
Type=forking

Environment=JAVA_HOME=/usr/lib/jvm/java-8-openjdk-amd64
Environment=CATALINA_PID=/opt/tomcat/temp/tomcat.pid
Environment=CATALINA_HOME=/opt/tomcat
Environment=CATALINA_BASE=/opt/tomcat
Environment='CATALINA_OPTS=-Xms512M -Xmx1024M -server -XX:+UseParallelGC'
Environment='JAVA_OPTS=-Djava.awt.headless=true -Djava.security.egd=file:/dev/./urandom'

ExecStart=/opt/tomcat/bin/startup.sh
ExecStop=/opt/tomcat/bin/shutdown.sh

User=root
Group=root
UMask=0007
RestartSec=10
Restart=always

[Install]
WantedBy=multi-user.target


$ sudo systemctl daemon-reload
$ sudo systemctl enable tomcat
$ sudo systemctl start tomcat
$ sudo systemctl status tomcat

http://localhost:8080/
