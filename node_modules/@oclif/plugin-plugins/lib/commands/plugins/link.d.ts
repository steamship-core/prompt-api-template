import { Command } from '@oclif/core';
import Plugins from '../../plugins';
export default class PluginsLink extends Command {
    static description: string;
    static usage: string;
    static examples: string[];
    static args: {
        path: import("@oclif/core/lib/interfaces/parser").Arg<string, Record<string, unknown>>;
    };
    static flags: {
        help: import("@oclif/core/lib/interfaces").BooleanFlag<void>;
        verbose: import("@oclif/core/lib/interfaces").BooleanFlag<boolean>;
    };
    plugins: Plugins;
    run(): Promise<void>;
}
