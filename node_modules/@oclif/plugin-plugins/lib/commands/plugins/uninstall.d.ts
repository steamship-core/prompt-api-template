import { Command, Interfaces } from '@oclif/core';
import Plugins from '../../plugins';
export default class PluginsUninstall extends Command {
    static description: string;
    static usage: string;
    static help: string;
    static variableArgs: boolean;
    static args: {
        plugin: import("@oclif/core/lib/interfaces/parser").Arg<string | undefined, Record<string, unknown>>;
    };
    static flags: {
        help: Interfaces.BooleanFlag<void>;
        verbose: Interfaces.BooleanFlag<boolean>;
    };
    static aliases: string[];
    plugins: Plugins;
    run(): Promise<void>;
    private removeTags;
}
