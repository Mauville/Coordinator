; Script generated by the Inno Setup Script Wizard.
; SEE THE DOCUMENTATION FOR DETAILS ON CREATING INNO SETUP SCRIPT FILES!

[Setup]
; NOTE: The value of AppId uniquely identifies this application.
; Do not use the same AppId value in installers for other applications.
; (To generate a new GUID, click Tools | Generate GUID inside the IDE.)
AppId={{B9A906AD-A5E6-4F17-80AC-198D619CA5BD}
AppName=Coordinator
AppVersion=5.2
;AppVerName=Coordinator 5.2
AppPublisher=Vargas Oscar
DefaultDirName={pf}\Coordinator
DisableProgramGroupPage=yes
InfoBeforeFile=C:\Users\Admin\Desktop\Coordinator\JDPA5.1\Source\What's new.txt
InfoAfterFile=C:\Users\Admin\Desktop\Coordinator\JDPA5.1\Source\Needs Firefox.txt
OutputBaseFilename=CoordinatorPSetup
Compression=lzma
SolidCompression=yes
SetupIconFile="C:\Users\Admin\Desktop\Coordinator\JDPA5.1\Source\logo.ico"

[Languages]
Name: "english"; MessagesFile: "compiler:Default.isl"
Name: "spanish"; MessagesFile: "compiler:Languages\Spanish.isl"

[Tasks]
Name: "desktopicon"; Description: "{cm:CreateDesktopIcon}"; GroupDescription: "{cm:AdditionalIcons}"; Flags: unchecked

[Files]
Source: "C:\Users\Admin\Desktop\Coordinator\JDPA5.1\Source\dist\Coordinator\Coordinator.exe"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\Admin\Desktop\Coordinator\JDPA5.1\Source\dist\Coordinator\*"; DestDir: "{app}"; Flags: ignoreversion recursesubdirs createallsubdirs
; NOTE: Don't use "Flags: ignoreversion" on any shared system files

[Icons]
Name: "{commonprograms}\Coordinator"; Filename: "{app}\Coordinator.exe"
Name: "{commondesktop}\Coordinator"; Filename: "{app}\Coordinator.exe"; Tasks: desktopicon

[Run]
Filename: "{app}\Coordinator.exe"; Description: "{cm:LaunchProgram,Coordinator}"; Flags: nowait postinstall skipifsilent
