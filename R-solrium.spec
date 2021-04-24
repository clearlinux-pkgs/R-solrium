#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-solrium
Version  : 1.1.4
Release  : 27
URL      : https://cran.r-project.org/src/contrib/solrium_1.1.4.tar.gz
Source0  : https://cran.r-project.org/src/contrib/solrium_1.1.4.tar.gz
Summary  : General Purpose R Interface to 'Solr'
Group    : Development/Tools
License  : MIT
Requires: R-R6
Requires: R-crul
Requires: R-dplyr
Requires: R-jsonlite
Requires: R-plyr
Requires: R-tibble
Requires: R-xml2
BuildRequires : R-R6
BuildRequires : R-crul
BuildRequires : R-dplyr
BuildRequires : R-jsonlite
BuildRequires : R-plyr
BuildRequires : R-tibble
BuildRequires : R-xml2
BuildRequires : buildreq-R

%description
solrium
=======
<!-- [![Build Status](https://travis-ci.org/ropensci/solrium.svg?branch=master)](https://travis-ci.org/ropensci/solrium)
[![codecov.io](https://codecov.io/github/ropensci/solrium/coverage.svg?branch=master)](https://codecov.io/github/ropensci/solrium?branch=master) -->
[![Project Status: Active – The project has reached a stable, usable state and is being actively developed.](https://www.repostatus.org/badges/latest/active.svg)](https://www.repostatus.org/#active)
[![cran checks](https://cranchecks.info/badges/worst/solrium)](https://cranchecks.info/pkgs/solrium)
[![rstudio mirror downloads](https://cranlogs.r-pkg.org/badges/solrium?color=2ED968)](https://github.com/metacran/cranlogs.app)
[![cran version](https://www.r-pkg.org/badges/version/solrium)](https://cran.r-project.org/package=solrium)

%prep
%setup -q -c -n solrium
cd %{_builddir}/solrium

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1589774696

%install
export SOURCE_DATE_EPOCH=1589774696
rm -rf %{buildroot}
export LANG=C.UTF-8
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=haswell -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library solrium
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library solrium
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library solrium
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc solrium || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/solrium/DESCRIPTION
/usr/lib64/R/library/solrium/INDEX
/usr/lib64/R/library/solrium/LICENSE
/usr/lib64/R/library/solrium/Meta/Rd.rds
/usr/lib64/R/library/solrium/Meta/features.rds
/usr/lib64/R/library/solrium/Meta/hsearch.rds
/usr/lib64/R/library/solrium/Meta/links.rds
/usr/lib64/R/library/solrium/Meta/nsInfo.rds
/usr/lib64/R/library/solrium/Meta/package.rds
/usr/lib64/R/library/solrium/Meta/vignette.rds
/usr/lib64/R/library/solrium/NAMESPACE
/usr/lib64/R/library/solrium/NEWS.md
/usr/lib64/R/library/solrium/R/solrium
/usr/lib64/R/library/solrium/R/solrium.rdb
/usr/lib64/R/library/solrium/R/solrium.rdx
/usr/lib64/R/library/solrium/doc/cores_collections.Rmd
/usr/lib64/R/library/solrium/doc/cores_collections.html
/usr/lib64/R/library/solrium/doc/document_management.Rmd
/usr/lib64/R/library/solrium/doc/document_management.html
/usr/lib64/R/library/solrium/doc/index.html
/usr/lib64/R/library/solrium/doc/local_setup.Rmd
/usr/lib64/R/library/solrium/doc/local_setup.html
/usr/lib64/R/library/solrium/doc/search.Rmd
/usr/lib64/R/library/solrium/doc/search.html
/usr/lib64/R/library/solrium/examples/add_delete.json
/usr/lib64/R/library/solrium/examples/add_delete.xml
/usr/lib64/R/library/solrium/examples/books.csv
/usr/lib64/R/library/solrium/examples/books.json
/usr/lib64/R/library/solrium/examples/books.xml
/usr/lib64/R/library/solrium/examples/books2.json
/usr/lib64/R/library/solrium/examples/books2_delete.json
/usr/lib64/R/library/solrium/examples/books2_delete.xml
/usr/lib64/R/library/solrium/examples/books_delete.json
/usr/lib64/R/library/solrium/examples/books_delete.xml
/usr/lib64/R/library/solrium/examples/schema.xml
/usr/lib64/R/library/solrium/examples/solrconfig.xml
/usr/lib64/R/library/solrium/examples/updatecommands_add.json
/usr/lib64/R/library/solrium/examples/updatecommands_add.xml
/usr/lib64/R/library/solrium/examples/updatecommands_delete.json
/usr/lib64/R/library/solrium/examples/updatecommands_delete.xml
/usr/lib64/R/library/solrium/help/AnIndex
/usr/lib64/R/library/solrium/help/aliases.rds
/usr/lib64/R/library/solrium/help/paths.rds
/usr/lib64/R/library/solrium/help/solrium.rdb
/usr/lib64/R/library/solrium/help/solrium.rdx
/usr/lib64/R/library/solrium/html/00Index.html
/usr/lib64/R/library/solrium/html/R.css
/usr/lib64/R/library/solrium/tests/cloud_mode/test-add.R
/usr/lib64/R/library/solrium/tests/cloud_mode/test-collections.R
/usr/lib64/R/library/solrium/tests/standard_mode/test-core_create.R
/usr/lib64/R/library/solrium/tests/test-all.R
/usr/lib64/R/library/solrium/tests/testthat/helper-solrium.R
/usr/lib64/R/library/solrium/tests/testthat/test-add.R
/usr/lib64/R/library/solrium/tests/testthat/test-client.R
/usr/lib64/R/library/solrium/tests/testthat/test-collections.R
/usr/lib64/R/library/solrium/tests/testthat/test-core_create.R
/usr/lib64/R/library/solrium/tests/testthat/test-cursorMark.R
/usr/lib64/R/library/solrium/tests/testthat/test-delete.R
/usr/lib64/R/library/solrium/tests/testthat/test-errors.R
/usr/lib64/R/library/solrium/tests/testthat/test-ping.R
/usr/lib64/R/library/solrium/tests/testthat/test-schema.R
/usr/lib64/R/library/solrium/tests/testthat/test-solr_all.R
/usr/lib64/R/library/solrium/tests/testthat/test-solr_error.R
/usr/lib64/R/library/solrium/tests/testthat/test-solr_facet.r
/usr/lib64/R/library/solrium/tests/testthat/test-solr_get.R
/usr/lib64/R/library/solrium/tests/testthat/test-solr_goup.R
/usr/lib64/R/library/solrium/tests/testthat/test-solr_highlight.r
/usr/lib64/R/library/solrium/tests/testthat/test-solr_json_request.R
/usr/lib64/R/library/solrium/tests/testthat/test-solr_mlt.r
/usr/lib64/R/library/solrium/tests/testthat/test-solr_search.r
/usr/lib64/R/library/solrium/tests/testthat/test-solr_stats.r
/usr/lib64/R/library/solrium/tests/testthat/test-update_atomic_json.R
/usr/lib64/R/library/solrium/tests/testthat/test-update_atomic_xml.R
/usr/lib64/R/library/solrium/tests/testthat/test-update_csv.R
/usr/lib64/R/library/solrium/tests/testthat/test-update_json.R
/usr/lib64/R/library/solrium/tests/testthat/test-update_xml.R
