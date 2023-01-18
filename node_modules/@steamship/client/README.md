# Steamship Typescript Client Library

Steamship is a cloud-hosted database that helps developers get work done with natural language content.

**Steamship is currently in a closed beta.** If you are interested in joining, please sign up at https://www.steamship.com

## Installing

```
npm install @steamship/client --save
```

## Using

### Initialization

Sign up for an account at https://www.steamship.com to get your API key. Then use it to initialize your client library:

```typescript
import Client from '@steamship/client';
const steamship = new Steamship(api_key);
```

### Embedding Indices

An Embedding Index is a persistent, read-optimized index over an embedded space. Once an index is created, you can search for similar items within that embedding space.

```typescript
const index = await steamship.createIndex({
  name: 'Question Answering Index',
  model: EmbeddingModels.QA,
  upsert: true,
});

await index.insert({ value: 'Armadillo shells are bulletproof.' });
await index.insert({ value: 'Dolphins sleep with one eye open.' });
await index.insert({ value: 'Alfred Hitchcock was frightened of eggs.' });
await index.insert({
  value: 'Jonathan can help you with new employee onboarding',
});
await index.insert({ value: 'The code for the New York office is 1234' });

let task = await index.embed();
await task.wait();

const results = await index.search({
  query: 'Who should I talk to about new employee setup?',
});
```

## Developing

This library was made with the [Typescript Starter](https://www.npmjs.com/package/typescript-starter). Many of the development instructions here are copy-pasted from their README.

To start working, run the `watch:build` task using [`npm`](https://docs.npmjs.com/getting-started/what-is-npm) or [`yarn`](https://yarnpkg.com/).

```sh
npm run watch:build
```

In another terminal tab/window, run the `watch:test` task:

```sh
npm run watch:test
```

These watch tasks make development much faster and more interactive. They're particularly helpful for [TDD](https://en.wikipedia.org/wiki/Test-driven_development)/[BDD](https://en.wikipedia.org/wiki/Behavior-driven_development) workflows.

These watch tasks will build and watch the entire project for changes (to both the library source files and test source files). As you develop, you can add tests for new functionality – which will initially fail – before developing the new functionality. Each time you save, any changes will be rebuilt and retested.

<p align="center">
  <!-- PR request: capture the magic of using a test-running watch task for development -->
  <img alt="typescript-starter's watch task" src="https://user-images.githubusercontent.com/904007/37270842-c05f5192-25a6-11e8-83bb-1981ae48e38e.png">
</p>

Since only changed files are rebuilt and retested, this workflow remains fast even for large projects.

## Enable stronger type checking (recommended)

To make getting started easier, the default `tsconfig.json` is using a very flexible configuration. This will allow you to get started without many warnings from Typescript.

To enable additional Typescript type checking features (a good idea for mission-critical or large projects), review the commented-out lines in your [typescript compiler options](./tsconfig.json).

## Auto-fix and format project

To automatically fix `eslint` and `prettier` formatting issues, run:

```sh
npm run fix
```

## View test coverage

To generate and view test coverage, run:

```sh
npm run cov
```

This will create an HTML report of test coverage – source-mapped back to Typescript – and open it in your default browser.

<p align="center">
  <img height="600" alt="source-mapped typescript test coverage example" src="https://cloud.githubusercontent.com/assets/904007/22909301/5164c83a-f221-11e6-9d7c-72c924fde450.png">
</p>

## Generate your API docs

The src folder is analyzed and documentation is automatically generated using [TypeDoc](https://github.com/TypeStrong/typedoc).

```sh
npm run doc
```

This command generates API documentation for your library in HTML format and opens it in a browser.

Since types are tracked by Typescript, there's no need to indicate types in JSDoc format. For more information, see the [TypeDoc documentation](http://typedoc.org/guides/doccomments/).

To generate and publish your documentation to [GitHub Pages](https://pages.github.com/) use the following command:

```sh
npm run doc:publish
```

Once published, your documentation should be available at the proper GitHub Pages URL for your repo. See [`typescript-starter`'s GitHub Pages](https://bitjson.github.io/typescript-starter/) for an example.

<p align="center">
  <img height="500" alt="TypeDoc documentation example" src="https://cloud.githubusercontent.com/assets/904007/22909419/085b9e38-f222-11e6-996e-c7a86390478c.png">
</p>

For more advanced documentation generation, you can provide your own [TypeDoc theme](http://typedoc.org/guides/themes/), or [build your own documentation](https://blog.cloudflare.com/generating-documentation-for-typescript-projects/) using the JSON TypeDoc export:

```sh
npm run doc:json
```

## Bump version, update changelog, commit, & tag release

It's recommended that you install [`commitizen`](https://github.com/commitizen/cz-cli) to make commits to your project.

```sh
npm install -g commitizen

# commit your changes:
git cz
```

This project is tooled for [conventional changelog](https://github.com/conventional-changelog/conventional-changelog) to make managing releases easier. See the [standard-version](https://github.com/conventional-changelog/standard-version) documentation for more information on the workflow, or [`CHANGELOG.md`](CHANGELOG.md) for an example.

```sh
# bump package.json version, update CHANGELOG.md, git tag the release
npm run version
```

You may find a tool like [**`wip`**](https://github.com/bitjson/wip) helpful for managing work in progress before you're ready to create a meaningful commit.

## One-step publish preparation script

Bringing together many of the steps above, this repo includes a one-step release preparation command.

```sh
# Prepare a standard release:
npm run prepare-release
```

This command runs the following tasks:

- `hard-reset`: cleans the repo by removing all untracked files and resetting `--hard` to the latest commit. (**Note: this could be destructive.**)
- `test`: build and fully test the project
- `doc:html`: generate the latest version of the documentation
- `doc:publish`: publish the documentation to GitHub Pages
- `version`: bump package.json version, update CHANGELOG.md, and git tag the release

When the script finishes, it will log the final command needed to push the release commit to the repo and publish the package on the `npm` registry:

```sh
git push --follow-tags origin master; npm publish --access=public
```

Look over the release if you'd like, then execute the command to publish everything.

You can also prepare a non-standard release:

```sh
# Or a non-standard release:

# Reset the repo to the latest commit and build everything
npm run hard-reset && npm run test && npm run cov:check && npm run doc:html

# Then version it with standard-version options. e.g.:
# don't bump package.json version
npm run version -- --first-release

# Other popular options include:

# PGP sign it:
# $ npm run version -- --sign

# alpha release:
# $ npm run version -- --prerelease alpha

# And don't forget to push the docs to GitHub pages:
npm run doc:publish
```
# prompt-package
