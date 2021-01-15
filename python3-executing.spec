%global srcname executing

Name:           python-%{srcname}
Version:        0.5.4
Release:        1%{?dist}
Summary:        Python executing

License:        MIT
URL:            https://pypi.python.org/pypi/executing
Source0:        %{pypi_source}

BuildArch:      noarch

%global _description %{expand:
This mini-package lets you get information about what a frame is currently doing, particularly the AST node being executed.}

%description %_description

%package -n python3-%{srcname}
Summary:        %{summary}
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-asttokens
BuildRequires:  python3-tox

%description -n python3-%{srcname} %_description

%prep
%autosetup -n %{srcname}-%{version}

%build
%py3_build

%install
%py3_install

%check
%{python3} setup.py test

%files -n python3-%{srcname}
%license LICENSE.txt
%doc README.md
%{python3_sitelib}/%{srcname}-*.egg-info/
%{python3_sitelib}/%{srcname}/


%changelog
* Fri Jan 15 2021 Onuralp SEZER <thunderbirdtr@fedoraproject.org> - 0.5.4-1
- Initial package