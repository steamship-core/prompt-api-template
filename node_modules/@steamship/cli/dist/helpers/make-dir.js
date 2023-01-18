import fs from 'fs';
export function makeDir(root, options = { recursive: true }) {
    return fs.promises.mkdir(root, options);
}
