#!/usr/bin/env python
from distutils.core import setup

setup(
	name = 'bambu-codemirror',
	version = '0.1',
	description = 'Adds static files for the CodeMirror editor',
	author = 'Steadman',
	author_email = 'mark@steadman.io',
	url = 'http://pypi.python.org/pypi/bambu-codemirror',
	namespace_packages = ['bambu'],
	packages = [
		'bambu.codemirror'
	],
	package_data = {
		'bambu.codemirror': [
			'static/codemirror/keymap/*.js',
			'static/codemirror/lib/*.css',
			'static/codemirror/lib/*.js',
			'static/codemirror/lib/util/*.css',
			'static/codemirror/lib/util/*.js',
			'static/codemirror/mode/clike/*.js',
			'static/codemirror/mode/clike/*.html',
			'static/codemirror/mode/clojure/*.js',
			'static/codemirror/mode/clojure/*.html',
			'static/codemirror/mode/coffeescript/*.js',
			'static/codemirror/mode/coffeescript/*.html',
			'static/codemirror/mode/coffeescript/LICENSE',
			'static/codemirror/mode/css/*.js',
			'static/codemirror/mode/css/*.html',
			'static/codemirror/mode/diff/*.js',
			'static/codemirror/mode/diff/*.html',
			'static/codemirror/mode/ecl/*.js',
			'static/codemirror/mode/ecl/*.html',
			'static/codemirror/mode/erlang/*.js',
			'static/codemirror/mode/erlang/*.html',
			'static/codemirror/mode/gfm/*.js',
			'static/codemirror/mode/gfm/*.html',
			'static/codemirror/mode/go/*.js',
			'static/codemirror/mode/go/*.html',
			'static/codemirror/mode/groovy/*.js',
			'static/codemirror/mode/groovy/*.html',
			'static/codemirror/mode/haskell/*.js',
			'static/codemirror/mode/haskell/*.html',
			'static/codemirror/mode/htmlembedded/*.js',
			'static/codemirror/mode/htmlembedded/*.html',
			'static/codemirror/mode/htmlmixed/*.js',
			'static/codemirror/mode/htmlmixed/*.html',
			'static/codemirror/mode/javascript/*.js',
			'static/codemirror/mode/javascript/*.html',
			'static/codemirror/mode/jinja2/*.js',
			'static/codemirror/mode/jinja2/*.html',
			'static/codemirror/mode/less/*.js',
			'static/codemirror/mode/less/*.html',
			'static/codemirror/mode/lua/*.js',
			'static/codemirror/mode/lua/*.html',
			'static/codemirror/mode/markdown/*.js',
			'static/codemirror/mode/markdown/*.html',
			'static/codemirror/mode/mysql/*.js',
			'static/codemirror/mode/mysql/*.html',
			'static/codemirror/mode/ntriples/*.js',
			'static/codemirror/mode/ntriples/*.html',
			'static/codemirror/mode/pascal/*.js',
			'static/codemirror/mode/pascal/*.html',
			'static/codemirror/mode/pascal/LICENSE',
			'static/codemirror/mode/perl/*.js',
			'static/codemirror/mode/perl/*.html',
			'static/codemirror/mode/perl/LICENSE',
			'static/codemirror/mode/php/*.js',
			'static/codemirror/mode/php/*.html',
			'static/codemirror/mode/pig/*.js',
			'static/codemirror/mode/pig/*.html',
			'static/codemirror/mode/plsql/*.js',
			'static/codemirror/mode/plsql/*.html',
			'static/codemirror/mode/properties/*.js',
			'static/codemirror/mode/properties/*.html',
			'static/codemirror/mode/python/*.js',
			'static/codemirror/mode/python/*.html',
			'static/codemirror/mode/python/*.txt',
			'static/codemirror/mode/r/*.js',
			'static/codemirror/mode/r/*.html',
			'static/codemirror/mode/r/LICENSE',
			'static/codemirror/mode/rpm/changes/*.js',
			'static/codemirror/mode/rpm/changes/*.html',
			'static/codemirror/mode/rpm/spec/*.js',
			'static/codemirror/mode/rpm/spec/*.css',
			'static/codemirror/mode/rpm/spec/*.html',
			'static/codemirror/mode/rst/*.js',
			'static/codemirror/mode/rst/*.html',
			'static/codemirror/mode/ruby/*.js',
			'static/codemirror/mode/ruby/*.html',
			'static/codemirror/mode/ruby/LICENSE',
			'static/codemirror/mode/rust/*.js',
			'static/codemirror/mode/rust/*.html',
			'static/codemirror/mode/scheme/*.js',
			'static/codemirror/mode/scheme/*.html',
			'static/codemirror/mode/shell/*.js',
			'static/codemirror/mode/shell/*.html',
			'static/codemirror/mode/smalltalk/*.js',
			'static/codemirror/mode/smalltalk/*.html',
			'static/codemirror/mode/smarty/*.js',
			'static/codemirror/mode/smarty/*.html',
			'static/codemirror/mode/sparql/*.js',
			'static/codemirror/mode/sparql/*.html',
			'static/codemirror/mode/stex/*.js',
			'static/codemirror/mode/stex/*.html',
			'static/codemirror/mode/tiddlywiki/*.js',
			'static/codemirror/mode/tiddlywiki/*.css',
			'static/codemirror/mode/tiddlywiki/*.html',
			'static/codemirror/mode/tiki/*.css',
			'static/codemirror/mode/tiki/*.js',
			'static/codemirror/mode/tiki/*.html',
			'static/codemirror/mode/vbscript/*.js',
			'static/codemirror/mode/vbscript/*.html',
			'static/codemirror/mode/velocity/*.js',
			'static/codemirror/mode/velocity/*.html',
			'static/codemirror/mode/verilog/*.js',
			'static/codemirror/mode/verilog/*.html',
			'static/codemirror/mode/xml/*.js',
			'static/codemirror/mode/xml/*.html',
			'static/codemirror/mode/xquery/*.js',
			'static/codemirror/mode/xquery/*.html',
			'static/codemirror/mode/xquery/LICENSE',
			'static/codemirror/mode/xquery/test/*.html',
			'static/codemirror/mode/xquery/test/*.js',
			'static/codemirror/mode/yaml/*.js',
			'static/codemirror/mode/yaml/*.html'
			'static/codemirror/theme/*.css'
		]
	},
	classifiers = [
		'Development Status :: 4 - Beta',
		'Environment :: Web Environment',
		'Framework :: Django'
	]
)