%global packname  fdrtool
%global rlibdir  %{_libdir}/R/library

Name:             R-%{packname}
Version:          1.2.10
Release:          1
Summary:          Estimation and Control of (Local) False Discovery Rates
Group:            Sciences/Mathematics
License:          GPL (>= 3)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/fdrtool_1.2.10.tar.gz
BuildRequires:    R-devel Rmath-devel texlive-collection-latex 

%description
This package allows to estimate both tail area-based false discovery rates
(Fdr) as well as local false discovery rates (fdr) for a variety of null
models (p-values, z-scores, correlation coefficients, t-scores).  The
proportion of null values and the parameters of the null distribution are
adaptively estimated from the data.  In addition, the package contains
functions for non-parametric density estimation (Grenander estimator), for
monotone regression (isotonic regression and antitonic regression with
weights), for computing the greatest convex minorant (GCM) and the least
concave majorant (LCM), and for the half-normal and correlation

%prep
%setup -q -c -n %{packname}

%build

%install
mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%check
%{_bindir}/R CMD check %{packname}

%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/html
%doc %{rlibdir}/%{packname}/DESCRIPTION
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/data
%{rlibdir}/%{packname}/help
%{rlibdir}/%{packname}/libs
