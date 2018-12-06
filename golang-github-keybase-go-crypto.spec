# https://github.com/keybase/go-crypto

%global goipath github.com/keybase/go-crypto
%global commit  670ebd3adf7a737d69ffe83a777a8e34eadc1b32

%global common_description %{expand:
A fork of the Go supplementary cryptography libraries.}

%gometa -i

# gometa strips the leading "go-" off
%global goname golang-github-keybase-go-crypto

Name:           %{goname}
Version:        0
Release:        0.3%{?dist}
Summary:        Supplementary Go cryptography libraries (Keybase fork)
License:        BSD
URL:            %{gourl}
Source0:        %{gosource}

# Backported from upstream project to fix test failures with bn256:
# https://github.com/keybase/go-crypto/issues/69
Patch0:         go-crypto-670ebd3-bn256-ModInverse-fix.patch

%description
%{common_description}


%package devel
Summary:       %{summary}

%description devel
%{common_description}

This package contains library source intended for
building other packages which use import path with
%{goipath} prefix.


%prep
%forgeautosetup -p1


%install
%goinstall


%check
# SSH agent tests fail in mock
%gochecks -d ssh/agent


%files devel -f devel.file-list
%license LICENSE
%doc README PATENTS AUTHORS CONTRIBUTING.md CONTRIBUTORS


%changelog
* Thu Jul 26 2018 Ed Marshall <esm@logic.net> - 0-0.3.20180727git670ebd3
- Switch to forge-specific packaging.
- Update to latest upstream commit.
- Upstream merged go-crypto-8bab6ce-go1.10-fixtests.patch.
- Backport bn256 ModInverse patch from upstream's upstream to fix test failure.

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.2.20180130git8bab6ce
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Mar 14 2018 Ed Marshall <esm@logic.net> - 0-0.1.20180130git8bab6ce
- Update to latest git commit to fix FTBFS.

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.2.20170628git433e2f3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Oct 03 2017 Ed Marshall <esm@logic.net> - 0-0.1.20170628git433e2f3
- First package for Fedora
