Name:           tsuru
Version:        0.6.2
Release:        1
Summary:        tsuru is an open source PaaS that makes it easy and fast to deploy and manage applications on your own servers.

Group:          tsuru
License:        https://github.com/tsuru/tsuru/blob/0.6.2/LICENSE
URL:            http://www.tsuru.io
Source0:        https://launchpad.net/~tsuru/+archive/ubuntu/ppa/+files/tsuru-server_0.6.2.1.orig.tar.gz
BuildRoot:      %{_tmppath}/%{name}-server-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires:  golang  

%define gopath %{_builddir}/tsuru-server-%{version}.%{release}
 
%description

tsuru is an open source polyglot cloud application platform (PaaS).
With tsuru, you don’t need to think about servers at all. You can write apps 
in the programming language of your choice, back it with add-on resources such
as SQL and NoSQL databases, memcached, redis, and many others. You manage your
app using the tsuru command-line tool and you deploy code using the Git revision
control system, all running on the tsuru infrastructure.

%prep
%setup -n tsuru-server-%{version}.%{release}


%build
export GOPATH=%{gopath}
go install github.com/tsuru/tsuru/cmd/tsr

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/bin

install -s -m 755 %{gopath}/bin/tsr $RPM_BUILD_ROOT/usr/bin/tsr


%clean
# rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc
/usr/bin/tsr


%changelog
* Fri Sep 12 2014 - wagnersza@gmail.com
- initial version