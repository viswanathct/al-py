#!/bin/bash

set -e

# Init
cd $(dirname $0)

# Tasks
setupEnvironment() {
	hooksPath="./.githooks"

	git config core.hooksPath "$hooksPath"
	chmod 775 "$hooksPath"/*
}

installDevDependencies() {

	pip install bumpversion
	pip install twine
}

installPackageForDevelopment() {
	pip install -e ./
}

# Main
setupEnvironment
installDevDependencies
installPackageForDevelopment
