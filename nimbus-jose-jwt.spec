%global GitCommit 1912aef94251
Name:          nimbus-jose-jwt
Version:       4.27
Release:       1%{?dist}
Summary:       Java library for Javascript Object Signing and Encryption (JOSE) and JSON Web Tokens (JWT) 
License:       ASL 2.0
URL:           https://bitbucket.org/connect2id/nimbus-jose-jwt
Source0:       https://bitbucket.org/connect2id/nimbus-jose-jwt/get/%{version}.tar.gz

BuildRequires: maven-local
BuildRequires: mvn(com.github.stephenc.jcip:jcip-annotations)
BuildRequires: mvn(commons-io:commons-io)
BuildRequires: mvn(net.minidev:json-smart)
BuildRequires: mvn(org.apache.maven.plugins:maven-gpg-plugin)
BuildRequires: mvn(org.bouncycastle:bcpkix-jdk15on)
BuildArch:     noarch

%description
Nimbus JOSE+JWT is an open source (Apache 2.0) Java library that implements the Javascript Object Signing and Encryption (JOSE) spec suite and the closely related JSON Web Token (JWT) spec.

%package javadoc
Summary:       Javadoc for %{name}

%description javadoc
This package contains javadoc for %{name}.

%prep
%setup -n connect2id-%{name}-%{GitCommit}

%pom_remove_plugin -r :nexus-staging-maven-plugin

%mvn_file :%{name} %{name}

%build

%mvn_build -s

%install
%mvn_install

%files -f .mfiles-%{name}
%doc CHANGELOG.txt README.txt
%license COPYRIGHT.txt  LICENSE.txt

%files javadoc -f .mfiles-javadoc
%license COPYRIGHT.txt  LICENSE.txt

%changelog
* Sun Nov 6 2016 Michal Karm Babacek <karm@fedoraproject.org> 4.27-1
- initial rpm
