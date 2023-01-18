import { Command } from '@oclif/core';
import Plugins from '../../plugins';
export default class PluginsInstall extends Command {
    static description: string;
    static usage: string;
    static examples: string[];
    static strict: boolean;
    static args: {
        plugin: import("@oclif/core/lib/interfaces/parser").Arg<string, Record<string, unknown>>;
    };
    static flags: {
        help: import("@oclif/core/lib/interfaces").BooleanFlag<void>;
        verbose: import("@oclif/core/lib/interfaces").BooleanFlag<boolean>;
        force: import("@oclif/core/lib/interfaces").BooleanFlag<boolean>;
    };
    static aliases: string[];
    plugins: Plugins;
    run(): Promise<void>;
    parsePlugin(input: string): Promise<{
        name: string;
        tag: string;
        type: 'npm';
    } | {
        url: string;
        type: 'repo';
    }>;
}
