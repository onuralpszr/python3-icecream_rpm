%global srcname icecream

Name:           python-%{srcname}
Version:        2.0.0
Release:        1%{?dist}
Summary:        IceCream -- Never use print to debug again

License:        MIT
URL:            https://pypi.python.org/pypi/icecream
Source0:        %{pypi_source}

BuildArch:      noarch

%global _description %{expand:

IceCream -- Never use print() to debug again

Do you ever use print() or log() to debug your code? Of course you do. 
IceCream, or ic for short, makes print debugging a little sweeter.
IceCream is well tested, permissively licensed, and supports Python 2, Python 3, PyPy2, and PyPy3.}

%description %_description

%package -n python3-%{srcname}
Summary:        %{summary}
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-tox
#BuildRequires:  python3-executing

Requires: python3-executing

%description -n python3-%{srcname} %_description

%prep
%autosetup -n %{srcname}-%{version}

%build
%py3_build

%install
%py3_install

%check
%{python3} setup.py test

# Note that there is no %%files section for the unversioned python module
%files -n python3-%{srcname}
%license LICENSE.txt
%doc README.md
%{python3_sitelib}/%{srcname}-*.egg-info/
%{python3_sitelib}/%{srcname}/


%changelog
* Fri Jan 15 2021 Onuralp SEZER <thunderbirdtr@fedoraproject.org> - 2.0.0-1
- Initial package
