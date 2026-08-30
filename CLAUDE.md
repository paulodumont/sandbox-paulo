# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository Overview

This is a personal sandbox repository ("My own sandbox") used for experimentation. It currently contains a minimal zero-dependency Node.js HTTP server.

## Commands

- Run the server: `node server.js` (or `npm start`) — listens on port 3000, override with the `PORT` env var
- Quick check: `curl http://localhost:3000/health`
- There is no build step, linter, or test suite; there are no external dependencies, so `npm install` is unnecessary.

## Architecture

- `server.js` — the entire application: a `node:http` server with three behaviors: `/` (welcome JSON), `/health` (status + uptime JSON), and a JSON 404 for everything else.
- `Dockerfile` — container image for deployment (`node:22-alpine`).
- `README.md` — user-facing run and deployment instructions, written in Portuguese.

## Working in This Repository

- Since this is a sandbox, expect experiments to be self-contained. When adding a new project or experiment, include its own tooling configuration (e.g., a package manifest) alongside it.
- When build tooling, tests, or a linter is added, update this file with the relevant commands (build, lint, test, and how to run a single test).
- Work here is handed off to others by cloning the repository, so keep `main` mergeable and the README's run instructions accurate — finished work should not sit only on side branches.
